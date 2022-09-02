<h1 align="center">PY Wasm</h1>
<p align="center">Python in the browser with WebAssembly 👾</p>

## Overview

PyScript is a framework that leverages Pyodide, Web Assembly and modern web technologies to run Python in the browser! 🐍

WebAssembly (Wasm) is a binary instruction format for a stack-based virtual machine. Wasm is supported by modern web browsers and is designed as a portable compilation target for programming languages, enabling deployment on the web for client and server applications at near-native code execution speed.

Given that Python is an interpreted language, it does not come with a standard compiler and cannot target WebAssembly. To solve this, Pyodide was introduced. Pyodide compiles the entire CPython interpreter using emscripten to WebAssembly, able to sit in the browser and act as a Python interpreter.

PyScript provides a thin layer of abstraction on top of Pyodide, encapsulating the necessary biolerplate code and exposing useful web components to more easily build and interact with Python in the browser. PyScript itself is written in TypeScript using the Svelte framework, and is styled with Tailwind CSS and bundled with rollup.js.

## Usage

### Installation

Pyscript is bundled as a `js` script and `css` file that need to be referenced from your web application. These files can be installed locally or linked via a CDN. Visit [pyscript.net](https://pyscript.net) for the latest release.

### Development

To run locally, start a server in your project directory:

```shell
python -m http.server
```

* this allows you to load Python scripts from external files while opening the page locally, which would otherwise be blocked by the cross-origin resource sharing (CORS) policy enforced by web browsers

### Web Components

PyScript exposes useful [web components](https://github.com/pyscript/pyscript/blob/main/docs/tutorials/getting-started.md) to more easily build and interact with Python in the browser.

* `<py-script>`
* `<py-env>`
* `<py-repl>`
* `<py-config>`
* `<py-inputbox>`
* `<py-box>`
* `<py-button>`
* `<py-title>`
