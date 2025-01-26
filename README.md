# Streamlit-JS-Eval

I have removed several ```python console.log(...)``` statments from the original component.

SJE is a custom Streamlit component, built to evaluate arbitrary Javascript expressions and return the result. It can become useful in doing certain functionalities which are _simple_ things in JavaScript, but unavailable or difficult to do in Streamlit. Examples include cookie management, writing to clipboard, getting device width (e.g. to check if we are on a mobile device), getting browser language, sharing something through Android's share feature, knowing user agent, etc. See [MDN docs](https://developer.mozilla.org/en-US/docs/Web/API) for more information about Web APIs. 

- _Version 0.1.7 - March 2024_: Proposed a workaround for issue #2.


## Install

```python
pip3 install streamlit_js_eval
```

## Example

```python
st.write(f"Screen width is {streamlit_js_eval(js_expressions='screen.width', key = 'SCR')}")
```
`key` is an arbitrary but unique string, required by Streamlit components API for each call to `streamlit_js_eval`.

### Common JavaScript functionalities

Some more common functionalities are already implemented as Python functions. Examples include:

```python
# Returns user's location after asking for permission when the user clicks the generated link with the given text
location = get_geolocation()
# The URL parts of the page
location_json = get_page_location()
```

See `streamlit_js_eval/__init__.py` for more functions. Check a demo in `example.py` or [see it live](https://aghasemi-streamlit-js-eval-example-yleu91.streamlitapp.com/).

## Known Limitations

- It seems SJE has issues with `st.button` when getting called from inside a branch in Streamlit (e.g. in a loop, `if-else` block, ...). In version 0.1.7, you may use the custom `bootstrapButton` as a workaround in such situations.
