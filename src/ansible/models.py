from django.db import models
from django.conf import settings

class Playbook(models.Model):
    name = models.CharField(max_length=200)
    inventory = models.CharField(max_length=200, default="hosts")
    user = models.CharField(max_length=200, default="ubuntu")
    directory = models.CharField(max_length=200, editable=False, default="dir")

    def __str__(self):
        return self.name

    def format_directory(self):
        directory = self.name.lower()
        directory = directory.replace(" ","-")
        return directory

    def save(self, *args, **kwargs):
        self.directory = self.format_directory()
        super(Playbook, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "playbooks"


class Registry(models.Model):
    playbook = models.ForeignKey("Playbook", default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    file_path = models.FilePathField(path=settings.PLAYBOOK_DIR, recursive=True)

    def __str__(self):
        return self.name

    def modify_item_file_path(self):
        return self.item

    def save(self, *args, **kwargs):
        self.item = self.modify_item_file_path()
        super(Registry, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "registries"


class Repository(models.Model):
    # Handle public Github Repo for now
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "repositories"