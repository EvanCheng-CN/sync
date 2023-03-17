# Generated by Django 3.1.2 on 2020-10-11 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20201011_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='syncjob',
            name='detail',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='任务详情'),
        ),
        migrations.AlterField(
            model_name='machinetaskfile',
            name='file',
            field=models.CharField(max_length=128, verbose_name='文件名称(不带前缀)'),
        ),
        migrations.AlterField(
            model_name='machinetaskfile',
            name='is_processed',
            field=models.SmallIntegerField(choices=[(0, '没有'), (1, '完成')], default=0, help_text='“进一步处理”指是否对下载回来的数据进一步处理，比如分析，打包发送到其他服务器', verbose_name='进一步处理'),
        ),
        migrations.AlterField(
            model_name='machinetaskfile',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.synctask', verbose_name='所属任务'),
        ),
        migrations.AlterField(
            model_name='machinetaskfile',
            name='timestamp',
            field=models.IntegerField(verbose_name='远程时间戳'),
        ),
    ]