envs:
	export LD_LIBRARY_PATH=/home/jimmy/workspace/devel/pybind11-qt-foo/lib:${LD_LIBRARY_PATH}
	export PYTHONPATH=/home/jimmy/workspace/devel/pybind11-qt-foo/lib:${PYTHONPATH}
src-build:
	cd src;	qmake;	make; make install
src-clean:
	rm -fv ./src/.qmake.stash
	rm -fv ./src/Makefile
	rm -rfv ./src/obj
	rm -fv ./src/*.so*
test-build: src-clean src-build test-clean
	cd test; qmake; make; ./test
test-clean:
	rm -fv ./test/.qmake.stash
	rm -fv ./test/test
	rm -fv ./test/Makefile
	rm -rfv ./test/obj
binding-build:
	# mkdir -v ./build; conan install . -if ./build; conan build . -if ./build
	conan install . -if ./build; conan build . -bf ./build
binding-clean:
	rm -rfv ./build
binding-test:
	python ./binding/test.py
lib-clean:
	cd lib; rm -rfv ./*
all: lib-clean src-clean src-build binding-clean binding-build
	@echo 'make all'
