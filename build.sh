python pandoc-sitegen/build.py sitegen-config.yml

cd docs
python -m http.server --bind 127.0.0.1
