[app]
title = E-Transaction
package.name = etransaction
package.domain = org.senateur
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.api = 33
android.minapi = 21
android.sdk = 20
android.archs = armeabi-v7a, arm64-v8a
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
