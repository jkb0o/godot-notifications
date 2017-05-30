def can_build(platform):
	return platform == "android"


def configure(env):
		env.android_add_java_dir("android")
		env.android_add_to_manifest("AndroidManifestChunk.xml")
