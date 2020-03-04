from datetime import datetime, timezone, timedelta

def commit_datetime(author_time: str, author_tz: str):
    """
    Convert a commit's timestamp to an aware datetime object.

    Args:
        author_time: Unix timestamp string
        author_tz: string in the format +hhmm

    Returns:
        datetime.datetime object with tzinfo
    """

    # timezone info looks like +hhmm or -hhmm
    tz_hours = int(author_tz[:3])
    th_minutes = int(author_tz[0] + author_tz[3:])

    return datetime.fromtimestamp(
        int(author_time),
        timezone(timedelta(hours=tz_hours,minutes=th_minutes))
    )


def commit_datetime_string(dt: datetime):
    """
    Return a string representation for a commit's timestamp.

    Args:
        dt: datetime object with tzinfo

    Returns:
        string representation (should be localized)
    """
    return dt.strftime('%c %z')


def repo_authors_summary(authors, config: dict):
    """
    A summary list of the authors' contributions on repo level.

    Iterates over all authors and produces an HTML <ul> list with
    their names and overall contribution details (lines/percentage).

    TODO:
    - The output should be configurable or at least localizable
        (suggestions:
        - load a template with named fields for the values
            (user may provide alternative template)
        - provide plugin configuration options for the various labels
        )

    Args:
        authors: sorted list of Author objects
        config: plugin's config dict

    Returns:
        Unordered HTML list as a string.
    """
    show_contribution = config['show_contribution']
    show_line_count = show_contribution and config['show_line_count']
    result = """
<span class='git-authors'>
    <ul>
        """
    for author in authors:
        contribution = (
            ' (%s)' % author.contribution(None, str)
            if show_contribution
            else ''
        )
        lines = (
            '%s lines' % author.lines()
            if show_line_count
            else ''
        )
        result += """
    <li><a href='mailto:{author_email}'>{author_name}</a>:
    {lines}{contribution}</li>
    """.format(
        author_email=author.email(),
        author_name=author.name(),
        lines=lines,
        contribution=contribution
    )
    result += """
    </span>
</ul>
    """
    return result
