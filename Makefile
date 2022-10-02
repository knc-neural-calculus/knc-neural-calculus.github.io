BUILD := python pandoc-sitegen/build.py sitegen-config.yml
HOST := cd docs && python -m http.server --bind 127.0.0.1

all:
	$(BUILD)
	$(HOST)

fresh:
	rm -r .build_time || true
	$(BUILD)
	$(HOST)

host:
	$(HOST)

build:
	$(BUILD)

build-fresh:
	rm -r .build_time || true
	$(BUILD)

clean:
	rm -r .build_time || true
	rm -rf docs/