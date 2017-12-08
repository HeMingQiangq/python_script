# complie_after

cd ${WORKSPACE}/script
APK_URL_Release=https://qa-jenkins.jiedaibao.com/${JOB_NAME}/builds/${BUILD_NUMBER}/archive/Products/jDB-${BUILD_TYPE}-${BUILD_NUMBER}.apk
python Build/ReplaceFileContent.py html/trunk_install_release.html DLURL ${APK_URL_Release}
python Build/ReplaceFileContent.py html/trunk_install_release.html HEADER_TOP JDB_${BUILD_NUMBER}_${BUILD_TYPE}

APK_URL_Debug=https://qa-jenkins.jiedaibao.com/${JOB_NAME}/builds/${BUILD_NUMBER}/archive/Products/jDB-debug-${BUILD_NUMBER}.apk
python Build/ReplaceFileContent.py html/trunk_install_debug.html DLURL ${APK_URL_Debug}
python Build/ReplaceFileContent.py html/trunk_install_debug.html HEADER_TOP JDB_${BUILD_NUMBER}_debug


rm -f  $WORKSPACE/jDB/build/outputs/apk/jDB-release-unaligned.apk
rm -f  $WORKSPACE/jDB/build/outputs/apk/jDB-debug-unaligned.apk

rm -rf $WORKSPACE/Products
mkdir $WORKSPACE/Products
mv $WORKSPACE/jDB/build/outputs/apk/jDB-release.apk $WORKSPACE/jDB/build/outputs/apk/jDB-release-${BUILD_NUMBER}.apk 
mv $WORKSPACE/jDB/build/outputs/apk/jDB-debug.apk $WORKSPACE/jDB/build/outputs/apk/jDB-debug-${BUILD_NUMBER}.apk 
cp $WORKSPACE/jDB/build/outputs/apk/*.apk $WORKSPACE/Products
cp $WORKSPACE/script/html/trunk_install_release.html $WORKSPACE/Products/install_release.html
cp $WORKSPACE/script/html/trunk_install_debug.html $WORKSPACE/Products/install_debug.html
cd ${WORKSPACE}/script/QRCode
java -jar QRCode.jar ${BUILD_URL}artifact/Products/install_release.html JDBClient_${BUILD_TYPE}_${BUILD_NUMBER}.png icon/icon.png
java -jar QRCode.jar ${BUILD_URL}artifact/Products/install_debug.html JDBClient_debug_${BUILD_NUMBER}.png icon/icon.png
mv *.png $WORKSPACE/Products

cd ${WORKSPACE}
rm -rf script