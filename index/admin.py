#!/usr/bin/env python
# coding=utf-8

from django.contrib import admin

from index.models import Solution

class SolutionAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'moderator', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'moderator__username', 'moderator__first_name', 'moderator__last_name')

    fieldsets = [
        ('Solution', {
            'fields': ('title', 'points', 'source')
        }),
        ('Moderator', {
            'classes': ('collapse',),
            'fields': ('moderator',)
        }),
        ('Change History', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        })
    ]

    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Solution, SolutionAdmin)
