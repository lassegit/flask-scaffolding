from flask import Flask, Blueprint, request
import jinja2
from datetime import datetime

tpl_filter = Blueprint('tpl_filter', __name__)

@tpl_filter.app_template_filter('timeago')
def timeago(dt, default="just now"):
    """
    Returns string representing "time since" e.g.
    3 days ago, 5 hours ago etc.
    """
    if dt is None:
        return ""
        
    now = datetime.utcnow()
    diff = abs(now - dt)

    periods = (
        (diff.days / 365, "year", "years"),
        (diff.days / 30, "month", "months"),
        (diff.days / 7, "week", "weeks"),
        (diff.days, "day", "days"),
        (diff.seconds / 3600, "hour", "hours"),
        (diff.seconds / 60, "minute", "minutes"),
        (diff.seconds, "second", "seconds"),
    )

    for period, singular, plural in periods:
        if period >= 1:
            return "%d %s ago" % (period, singular if period == 1 else plural)

    return default

