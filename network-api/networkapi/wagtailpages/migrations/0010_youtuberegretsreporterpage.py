# Generated by Django 2.2.14 on 2020-09-08 20:00

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmetadata.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailpages', '0009_articleauthors_articlepage_publicationauthors_publicationpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeRegretsReporterPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headline', models.CharField(blank=True, help_text='Page headline', max_length=500)),
                ('headline_en', models.CharField(blank=True, help_text='Page headline', max_length=500, null=True)),
                ('headline_de', models.CharField(blank=True, help_text='Page headline', max_length=500, null=True)),
                ('headline_pt', models.CharField(blank=True, help_text='Page headline', max_length=500, null=True)),
                ('headline_es', models.CharField(blank=True, help_text='Page headline', max_length=500, null=True)),
                ('headline_fr', models.CharField(blank=True, help_text='Page headline', max_length=500, null=True)),
                ('headline_fy_NL', models.CharField(blank=True, help_text='Page headline', max_length=500, null=True)),
                ('headline_nl', models.CharField(blank=True, help_text='Page headline', max_length=500, null=True)),
                ('headline_pl', models.CharField(blank=True, help_text='Page headline', max_length=500, null=True)),
                ('intro_text', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock())])),
                ('intro_text_en', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock())], null=True)),
                ('intro_text_de', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock())], null=True)),
                ('intro_text_pt', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock())], null=True)),
                ('intro_text_es', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock())], null=True)),
                ('intro_text_fr', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock())], null=True)),
                ('intro_text_fy_NL', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock())], null=True)),
                ('intro_text_nl', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock())], null=True)),
                ('intro_text_pl', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock())], null=True)),
                ('intro_images', wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True))]))])),
                ('intro_images_en', wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True))]))], null=True)),
                ('intro_images_de', wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True))]))], null=True)),
                ('intro_images_pt', wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True))]))], null=True)),
                ('intro_images_es', wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True))]))], null=True)),
                ('intro_images_fr', wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True))]))], null=True)),
                ('intro_images_fy_NL', wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True))]))], null=True)),
                ('intro_images_nl', wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True))]))], null=True)),
                ('intro_images_pl', wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True))]))], null=True)),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Search image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
    ]
