from django.db import models
from django.db.models import F
import uuid
#from django_extensions.db.fields import UUIDField

class WithTimeModel(models.Model):
    """
    Base model with time tag.
    """
    created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    class Meta:
        abstract=True

class Words(models.Model):
    """
    This is the main table for words.#1
    """

    wid = models.AutoField(primary_key=True)
    word = models.CharField(max_length=30)
    level = models.ForeignKey('Levels')
    pronuncation = models.ManyToManyField(
        'Pronuncations',
    )
    definition = models.ManyToManyField(
        'Definitions',
    )
    sentence = models.ManyToManyField(
        'Sentences',
    )
    note = models.ManyToManyField(
        'Notes',
    )

    class Meta:
        unique_together = ('level', 'word')
        ordering = ['word']

    def __str__(self):
        return self.word

class Levels(models.Model):
    """
    Table from levels.#1.1
    """

    lid = models.AutoField(primary_key=True)
    counts = models.IntegerField(null=True)
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return  "%s(%s)" % (self.name, self.objects.count())

class Pronuncations(models.Model):
    """
    Table for pronuncations.#1.2
    I don't know whether the same prons sounded same with us or uk.
    """

    LANGUAGES = (
        ('zh_cn', 'simplified Chinese'),
        ('us', 'American English'),
        ('uk', 'British English')
    )

    pid = models.AutoField(primary_key=True)
    ptype = models.CharField(max_length=5, choices=LANGUAGES, default='us')
    pronuncation = models.CharField(max_length=50)
    # audio = models.ManyToManyField(
    #     'Audios',
    # )
    class Meta:
        unique_together = ('ptype', 'pronuncation')

    def __str__(self):
        return self.pronuncation

# class Audios(models.Model):
#     """
#     Table for pronuncations.#1.2.1
#     """

#     aid = models.AutoField(primary_key=True)
#     audio = models.CharField(max_length=255, unique=True)

#     def __str__(self):
#         return self.audio

class Definitions(models.Model):
    """
    Table for denifitions.#1.3
    The pos should dive to 2 parts.
    """

    LANGUAGES = (
        ('zh_cn', 'simplified Chinese'),
        ('us', 'American English'),
        ('uk', 'British English')
    )
    did = models.AutoField(primary_key=True)
    pos = models.CharField(max_length=10, blank=True)
    definition = models.CharField(max_length=255)
    language = models.CharField(max_length=5, choices=LANGUAGES)
    class Meta:
        unique_together = ('pos', 'definition')

    def __str__(self):
        return self.definition

class Sentences(WithTimeModel):
    """
    Table for sentences.#1.4
    Should be Many to Many
    """

    sid = models.AutoField(primary_key=True)
    #s_head = models.CharField(max_length=100)
    #s_tail = models.CharField(max_length=100)
    sentence = models.CharField(max_length=255)
    user = models.ForeignKey(
        'Users',
        null=True,
    )
    translation = models.ManyToManyField(
        'Translations',
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    is_offical = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'sentence')

    def __str__(self):
        return "%s" % (self.sentence)

class Translations(models.Model):
    """
    Table for sentence's translation.#1.4.1
    Should be Many to Many
    """

    tid = models.AutoField(primary_key=True)
    translation = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.translation

class Users(models.Model):
    """
    Table for user info.#2
    """

    uid = models.AutoField(primary_key=True)
    register = models.OneToOneField(
        'Registers',
        on_delete=models.CASCADE,
    )
    level = models.ForeignKey(
        Levels,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=20)
    daily_task = models.PositiveSmallIntegerField(default=20)
    is_male = models.BooleanField(default=False)

    def get_absolute_url(self):
        return "/api/user/%i/" % self.id

    def __str__(self):
        return self.name

class Registers(models.Model):
    """
    Table for registe.#2.1
    """

    RGTYPES = (
        ('m', 'Email'),
        ('p', 'Phone')
    )
    rid = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100, unique=True)
    rgtype = models.CharField(max_length=1, choices=RGTYPES)
    registed_time = models.DateField(auto_now_add=True)
    actived_time = models.DateField(auto_now=True)
    code = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.content

class Notes(WithTimeModel):
    """
    Table for Notes.#3
    """

    nid = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    note = models.TextField(max_length=1000)
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
    )
    is_shared = models.BooleanField(default=False)
    class Meta:
        unique_together = ('user', 'note')

    def __str__(self):
        return self.nid

class Votes(WithTimeModel):
    """
    Table for votes.#4
    """

    vid = models.AutoField(primary_key=True)
    target_uuid = models.CharField(max_length=36)
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
    )
    class Meta:
        unique_together = ('user', 'target_uuid')

    def __str__(self):
        return self.vid

class Comments(WithTimeModel):
    """
    Table for comments.#5
    """

    cid = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    target_uuid = models.CharField(max_length=36)
    content = models.TextField()
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
    )
    class Meta:
        unique_together = ('user', 'target_uuid')

    def __str__(self):
        return self.cid

class Records(WithTimeModel):
    """
    Table for records.#5
    """

    rdid = models.AutoField(primary_key=True)
    is_know = models.BooleanField(default=False)
    word = models.ForeignKey(
        Words,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.rdid