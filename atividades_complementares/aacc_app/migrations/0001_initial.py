# Generated by Django 5.0.2 on 2024-02-14 18:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Aacc",
            fields=[
                ("id_aacc", models.AutoField(primary_key=True, serialize=False)),
                ("aluno", models.CharField(max_length=8)),
                ("doc", models.FileField(upload_to="documentos/")),
                ("data_envio", models.DateField()),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "Aguardando"),
                            (1, "Enviada"),
                            (2, "Avaliada"),
                            (3, "Confirmada"),
                        ],
                        default=0,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AaccParaAvaliacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Aguardando"), (1, "Deferida"), (2, "Indeferida")],
                        default=0,
                    ),
                ),
                (
                    "comentarios",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "id_aacc",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="aacc_app.aacc"
                    ),
                ),
                (
                    "id_avaliador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
