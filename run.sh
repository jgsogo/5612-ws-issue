
echo "==== functional-helpers/dev@theo/testing ==="
conan create functional-helpers/conanfile.py functional-helpers/dev@theo/testing
echo "==== theo_conanfile/dev@theo/testing ==="
conan create theo_conanfile/conanfile.py theo/testing
echo "==== bug/dev@theo/testing ==="
conan create bug/conanfile.py bug/version@theo/testing

echo "==== WORKSPACE ===="
conan workspace install .
