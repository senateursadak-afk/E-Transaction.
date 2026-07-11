[app]
# (str) Title of your application
title = MonApplication

# (str) Package name
package.name = monapplication

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Ajoutez ici vos dépendances (ex: kivy, requests)
requirements = python3,kivy

# (str) Application versioning
version = 0.1

# (list) Permissions
android.permissions = INTERNET

# (int) Android API to use
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android SDK build-tools version
android.sdk_build_tools_version = 33.0.1

# (str) Android NDK version
android.ndk = 25b

# (bool) Indicate whether the application should be fullscreen
fullscreen = 0

[buildozer]
# (int) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2

# (int) If 1, buildozer will run as root
sudo = 0

# (str) Buildozer source dir
build_dir = .buildozer

# (str) Bin directory
bin_dir = ./bin
