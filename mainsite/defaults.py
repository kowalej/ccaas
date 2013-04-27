from mezzanine.conf import register_setting


register_setting(
    name="SCHOOLS_FOREIGN_SCHOOLS_PER_PAGE",
    description="The number of foreign (Kenyan) schools to show on a single page.",
    editable=True,
    default=10,
	label="Foreign Schools Per Page",
)

register_setting(
    name="SCHOOLS_LOCAL_SCHOOLS_PER_PAGE",
    description="The number of local (Canadian) schools to show on a single page.",
    editable=True,
    default=10,
	label="Local Schools Per Page",
)

register_setting(
    name="SOCIAL_TWITTER_PROFILE_URL",
    description="The url of the Twitter profile (start it with http://).",
    editable=True,
    default="http://www.twitter.com",
	label="Twitter Profile URL",
)

register_setting(
    name="SOCIAL_FACEBOOK_PROFILE_URL",
    description="The url of the Facebook profile (start it with http://).",
    editable=True,
    default="http://www.facebook.com",
	label="Facebook Profile URL",
)

register_setting(
    name="SOCIAL_YOUTUBE_PROFILE_URL",
    description="The url of the YouTube profile (start it with http://).",
    editable=True,
    default="http://www.youtube.com",
	label="YouTube Profile URL",
)

register_setting(
    name="TOP_BAR_MOTD",
    description="The message to be displayed at the top of the screen beside the search and social media icons.",
    editable=True,
    default="",
	label="Top Bar MOTD",
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    description="Sequence of setting names available within templates.",
    editable=False,
    default=("SCHOOLS_FOREIGN_SCHOOLS_PER_PAGE","SCHOOLS_LOCAL_SCHOOLS_PER_PAGE","SOCIAL_TWITTER_PROFILE_URL",
	"SOCIAL_FACEBOOK_PROFILE_URL","SOCIAL_YOUTUBE_PROFILE_URL","TOP_BAR_MOTD",),
    append=True,
)


