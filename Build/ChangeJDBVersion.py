import ReplaceAppVersion, sys

BASE_PATH = sys.argv[1]
MANIFEST_PATH = BASE_PATH + '/jDB/src/main/AndroidManifest.xml'
print MANIFEST_PATH
JDB_VERSION_NUMBER = sys.argv[2]

ReplaceAppVersion.replaceVersionNumberOfFile(MANIFEST_PATH, JDB_VERSION_NUMBER, r'android:value=.\d\.\d\.\d.')
