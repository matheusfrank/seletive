# Generated by Django 4.1.3 on 2022-11-09 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("empresa", "0003_tecnologias_empresa_logo_empresa_tecnologias"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empresa",
            name="logo",
            field=models.ImageField(null=True, upload_to="logo_empresa"),
        ),
        migrations.CreateModel(
            name="Vagas",
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
                ("titulo", models.CharField(max_length=30)),
                (
                    "nivel_experiencia",
                    models.CharField(
                        choices=[("J", "Júnior"), ("P", "Pleno"), ("S", "Sênior")],
                        max_length=2,
                    ),
                ),
                ("data_final", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("I", "Interesse"),
                            ("C", "Currículo enviado"),
                            ("E", "Entrevista"),
                            ("D", "Desafio técnico"),
                            ("F", "Finalizado"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="empresa.empresa",
                    ),
                ),
                (
                    "tecnologias_dominadas",
                    models.ManyToManyField(to="empresa.tecnologias"),
                ),
                (
                    "tecnologias_estudar",
                    models.ManyToManyField(
                        related_name="estudar", to="empresa.tecnologias"
                    ),
                ),
            ],
        ),
    ]
