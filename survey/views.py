from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET, require_http_methods

from .models import Answer, FeedbackSession, Question, Subject, Teacher


@require_http_methods(["GET", "POST"])
def survey_view(request):
    if request.method == "POST":
        teacher = get_object_or_404(Teacher, pk=request.POST.get("teacher"))
        subject = get_object_or_404(
            Subject,
            pk=request.POST.get("subject"),
            teacher=teacher,
        )
        lesson_type = request.POST.get("lesson_type")
        comment = request.POST.get("comment", "").strip()

        questions = list(Question.objects.filter(lesson_type=lesson_type))

        session = FeedbackSession.objects.create(
            teacher=teacher,
            subject=subject,
            lesson_type=lesson_type,
            comment=comment,
        )

        answers = []
        for question in questions:
            score = request.POST.get(f"q_{question.id}")
            if score:
                answers.append(
                    Answer(
                        session=session,
                        question=question,
                        score=int(score),
                    )
                )

        if answers:
            Answer.objects.bulk_create(answers)

        return render(
            request,
            "survey/success.html",
            {
                "teacher": teacher,
                "subject": subject,
            },
        )

    teachers = Teacher.objects.all()
    lesson_types = Question._meta.get_field("lesson_type").choices
    return render(
        request,
        "survey/index.html",
        {
            "teachers": teachers,
            "lesson_types": lesson_types,
        },
    )


@require_GET
def get_subjects(request, teacher_id):
    subjects = Subject.objects.filter(teacher_id=teacher_id).values("id", "name")
    return JsonResponse(list(subjects), safe=False)


@require_GET
def get_questions(request, lesson_type):
    questions = Question.objects.filter(lesson_type=lesson_type).values("id", "text")
    return JsonResponse(list(questions), safe=False)
