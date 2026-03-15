mkdir -p ~/.streamlit/


echo "\
[server]\n\
port = $PORT\n\
headless = true\n\
enableCORS = false\n\
" > ~/.streamlit/config.toml