# tap-ecb

`tap-ecb` is a Singer tap for ECB data.

v0.0.1 only supports historic exchange rate data.

Really this is just a singer-sdk wrapper around the endpoint https://www.ecb.europa.eu//stats/eurofxref/eurofxref-hist.xml.
In the future, it would be great to broaden this to the whole SDMX catalog.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

Install from GitHub:

```bash
pip install git+https://github.com/kingalban/tap-ecb.git@main
```

## Configuration

There isn't any config or authentication needed. State is also not supported by the API, so just hit play and enjoy.

### Accepted Config Options

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-ecb --about
```

## Usage

You can easily run `tap-ecb` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-ecb --version
tap-ecb --help
tap-ecb --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-ecb` CLI interface directly using `poetry run`:

```bash
poetry run tap-ecb --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-ecb
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-ecb --version
# OR run a test `elt` pipeline:
meltano elt tap-ecb target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
