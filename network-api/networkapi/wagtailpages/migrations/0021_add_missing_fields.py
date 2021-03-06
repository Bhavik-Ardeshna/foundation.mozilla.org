# Generated by Django 2.2.16 on 2020-12-10 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0020_add_localizable_field_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalproductpage',
            name='offline_use_description_de',
            field=models.TextField(blank=True, help_text='Describe how this product can be used offline.', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='generalproductpage',
            name='offline_use_description_en',
            field=models.TextField(blank=True, help_text='Describe how this product can be used offline.', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='generalproductpage',
            name='offline_use_description_es',
            field=models.TextField(blank=True, help_text='Describe how this product can be used offline.', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='generalproductpage',
            name='offline_use_description_fr',
            field=models.TextField(blank=True, help_text='Describe how this product can be used offline.', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='generalproductpage',
            name='offline_use_description_fy_NL',
            field=models.TextField(blank=True, help_text='Describe how this product can be used offline.', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='generalproductpage',
            name='offline_use_description_nl',
            field=models.TextField(blank=True, help_text='Describe how this product can be used offline.', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='generalproductpage',
            name='offline_use_description_pl',
            field=models.TextField(blank=True, help_text='Describe how this product can be used offline.', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='generalproductpage',
            name='offline_use_description_pt',
            field=models.TextField(blank=True, help_text='Describe how this product can be used offline.', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='generalproductpage',
            name='social_data_collected_de',
            field=models.TextField(blank=True, help_text='What kind of social data does this product collect?', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='generalproductpage',
            name='social_data_collected_en',
            field=models.TextField(blank=True, help_text='What kind of social data does this product collect?', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='generalproductpage',
            name='social_data_collected_es',
            field=models.TextField(blank=True, help_text='What kind of social data does this product collect?', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='generalproductpage',
            name='social_data_collected_fr',
            field=models.TextField(blank=True, help_text='What kind of social data does this product collect?', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='generalproductpage',
            name='social_data_collected_fy_NL',
            field=models.TextField(blank=True, help_text='What kind of social data does this product collect?', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='generalproductpage',
            name='social_data_collected_nl',
            field=models.TextField(blank=True, help_text='What kind of social data does this product collect?', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='generalproductpage',
            name='social_data_collected_pl',
            field=models.TextField(blank=True, help_text='What kind of social data does this product collect?', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='generalproductpage',
            name='social_data_collected_pt',
            field=models.TextField(blank=True, help_text='What kind of social data does this product collect?', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='productpageprivacypolicylink',
            name='label_de',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productpageprivacypolicylink',
            name='label_en',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productpageprivacypolicylink',
            name='label_es',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productpageprivacypolicylink',
            name='label_fr',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productpageprivacypolicylink',
            name='label_fy_NL',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productpageprivacypolicylink',
            name='label_nl',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productpageprivacypolicylink',
            name='label_pl',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productpageprivacypolicylink',
            name='label_pt',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
    ]
