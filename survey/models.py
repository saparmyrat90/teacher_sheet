from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class LessonType(models.TextChoices):
    GENERAL = "umumy", "Umumy"
    PRACTICAL = "amaly", "Amaly"
    LAB = "tejribe", "Tejribe"
    DISCUSSION = "sohbet", "Sohbet"


class Teacher(models.Model):
    full_name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["full_name"]
        verbose_name = "Mugallym"
        verbose_name_plural = "Mugallymlar"

    def __str__(self) -> str:
        return self.full_name


class Subject(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="subjects",
    )

    class Meta:
        ordering = ["name", "teacher__full_name"]
        unique_together = ("name", "teacher")
        verbose_name = "Ders"
        verbose_name_plural = "Dersler"

    def __str__(self) -> str:
        return f"{self.name} - {self.teacher.full_name}"


class Question(models.Model):
    text = models.TextField()
    lesson_type = models.CharField(
        max_length=20,
        choices=LessonType.choices,
        default=LessonType.GENERAL,
    )

    class Meta:
        ordering = ["lesson_type", "id"]
        verbose_name = "Sorag"
        verbose_name_plural = "Soraglar"

    def __str__(self) -> str:
        return self.text[:80]


class FeedbackSession(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="feedback_sessions",
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="feedback_sessions",
    )
    lesson_type = models.CharField(
        max_length=20,
        choices=LessonType.choices,
        default=LessonType.GENERAL,
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Soragnama sessiyasy"
        verbose_name_plural = "Soragnama sessiyalary"

    def __str__(self) -> str:
        return f"{self.teacher.full_name} / {self.subject.name} / {self.created_at:%Y-%m-%d %H:%M}"


class Answer(models.Model):
    session = models.ForeignKey(
        FeedbackSession,
        on_delete=models.CASCADE,
        related_name="answers",
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers",
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        ordering = ["session", "question"]
        unique_together = ("session", "question")
        verbose_name = "Jogap"
        verbose_name_plural = "Jogaplar"

    def __str__(self) -> str:
        return f"{self.session} / {self.question} / {self.score}"
