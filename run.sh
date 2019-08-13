
conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan 

echo "==== CREATE PACKAGES ==="
conan create test-helpers theo_test-helpers/dev@theo/testing
conan create crypto theo_crypto/dev@theo/testing
conan create fake-authentication theo_fake-authentication/dev@theo/testing


echo "==== WORKSPACE ===="
mkdir build
cd build
conan workspace install ..
