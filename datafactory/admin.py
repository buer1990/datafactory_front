from django.contrib import admin

# Register your models here.
from .models import Tool, ToolAttr,ToolPath


class ToolAttrInline(admin.TabularInline):
    model = ToolAttr
    extra = 3


class ToolPathInline(admin.TabularInline):
    model = ToolPath
    extra = 1


class ToolAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Tool name", {'fields': ['tool_name']}),
        ('Date information', {'fields': ['create_time'], 'classes': ['collapse']}),
    ]
    inlines = [ToolAttrInline, ToolPathInline]

    list_display = ('tool_name', 'create_time', 'was_published_recently')
    # 卧槽有点强大啊！！！两个变量完成两个赛选功能
    list_filter = ['create_time']
    search_fields = ['tool_name']


admin.site.register(Tool, ToolAdmin)
