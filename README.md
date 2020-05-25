# TRAINS
## Auto-Magical Experiment Manager & Version Control for AI

## :tada: Now with Full DevOps - check the latest addition [TRAINS AGENT](https://github.com/allegroai/trains-agent)
## :station: [Documentation is here!](https://allegro.ai/docs) `wubba lubba dub dub` and a [Slack Channel](https://join.slack.com/t/allegroai-trains/shared_invite/enQtOTQyMTI1MzQxMzE4LTY5NTUxOTY1NmQ1MzQ5MjRhMGRhZmM4ODE5NTNjMTg2NTBlZGQzZGVkMWU3ZDg1MGE1MjQxNDEzMWU2NmVjZmY) :train2: 
## There is also an updated :sparkle: [TRAINS AWS autoscaler](https://github.com/allegroai/trains-agent/blob/master/examples/dynamic_cloud_cluster.ipynb)

"Because it’s a jungle out there"

[![GitHub license](https://img.shields.io/github/license/allegroai/trains.svg)](https://img.shields.io/github/license/allegroai/trains.svg)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/trains.svg)](https://img.shields.io/pypi/pyversions/trains.svg)
[![PyPI version shields.io](https://img.shields.io/pypi/v/trains.svg)](https://img.shields.io/pypi/v/trains.svg)
[![PyPI status](https://img.shields.io/pypi/status/trains.svg)](https://pypi.python.org/pypi/trains/)

### Help improve Trains by filling our 2-min [user survey](https://allegro.ai/lp/trains-user-survey/)

TRAINS is our solution to a problem we share with countless other researchers and developers in the machine
learning/deep learning universe: Training production-grade deep learning models is a glorious but messy process.
TRAINS tracks and controls the process by associating code version control, research projects,
performance metrics, and model provenance.

We designed TRAINS specifically to require effortless integration so that teams can preserve their existing methods
and practices. Use it on a daily basis to boost collaboration and visibility, or use it to automatically collect
your experimentation logs, outputs, and data to one centralized server.

**We have a demo server up and running at [https://demoapp.trains.allegro.ai](https://demoapp.trains.allegro.ai).**

**You can try out TRAINS and [test your code](#integrate-trains), with no additional setup.**
<a href="https://demoapp.trains.allegro.ai"><img src="https://github.com/allegroai/trains/blob/master/docs/webapp_screenshots.gif?raw=true" width="100%"></a>

## TRAINS Automatically Logs Everything
**With only two lines of code, this is what you are getting:**

* Git repository, branch, commit id, entry point and local git diff
* Python environment (including specific packages & versions)
* stdout and stderr
* Resource Monitoring (CPU/GPU utilization, temperature, IO, network, etc.)
* Hyper-parameters
    * ArgParser for command line parameters with currently used values
    * Explicit parameters dictionary
    * Tensorflow Defines (absl-py)
* Initial model weights file
* Model snapshots (With optional automatic upload to central storage: Shared folder, S3, GS, Azure, Http)
* Artifacts log & store (Shared folder, S3, GS, Azure, Http)
* Tensorboard/TensorboardX scalars, metrics, histograms, images (with audio coming soon)
* Matplotlib & Seaborn
* Supported frameworks: Tensorflow, PyTorch, Keras, XGBoost and Scikit-Learn (MxNet is coming soon)
* Seamless integration (including version control) with **Jupyter Notebook**
    and [*PyCharm* remote debugging](https://github.com/allegroai/trains-pycharm-plugin)

**Additionally, log data explicitly using [TRAINS Explicit Logging](https://github.com/allegroai/trains/blob/master/docs/logger.md).**

## Using TRAINS <a name="using-trains"></a>

TRAINS is a two part solution:

1. TRAINS [python package](https://pypi.org/project/trains/) auto-magically connects with your code

   **TRAINS requires only two lines of code for full integration.**

    To connect your code with TRAINS:

    - Install TRAINS <a name="integrate-trains"></a>

            pip install trains
		<details>
		<summary>Add optional cloud storage support (S3/GoogleStorage/Azure):</summary>

		```bash
		pip install trains[s3]
		pip install trains[gs]
		pip install trains[azure]
		```
		
		</details>

    - Add the following lines to your code

            from trains import Task
            task = Task.init(project_name="my project", task_name="my task")

        * If project_name is not provided, the repository name will be used instead
        * If task_name (experiment) is not provided, the current filename will be used instead

    - Run your code. When TRAINS connects to the server, a link is printed. For example

            TRAINS Results page:
            https://demoapp.trains.allegro.ai/projects/76e5e2d45e914f52880621fe64601e85/experiments/241f06ae0f5c4b27b8ce8b64890ce152/output/log

    - Open the link and view your experiment parameters, model and tensorboard metrics

    **See examples [here](https://github.com/allegroai/trains/tree/master/examples)**

2. [TRAINS-server](https://github.com/allegroai/trains-server) for logging, querying, control and UI ([Web-App](https://github.com/allegroai/trains-web))
    
    **We already have a demo server up and running for you at [https://demoapp.trains.allegro.ai](https://demoapp.trains.allegro.ai).**
    
    **You can try out TRAINS without the need to install your own *trains-server*, just add the two lines of code, and it will automatically connect to the TRAINS demo-server.**
    
    *Note that the demo server resets every 24 hours and all of the logged data is deleted.*

    When you are ready to use your own TRAINS server, go ahead and [install *TRAINS-server*](https://github.com/allegroai/trains-server).

<img src="https://github.com/allegroai/trains/blob/master/docs/system_diagram.png?raw=true" width="50%">


## Configuring Your Own TRAINS server <a name="configuration"></a>

1. Install and run *TRAINS-server* (see [Installing the TRAINS Server](https://github.com/allegroai/trains-server))

2. Run the initial configuration wizard for your TRAINS installation and follow the instructions to setup TRAINS package
(http://**_trains-server-ip_**:__port__ and user credentials)

	    trains-init

After installing and configuring, you can access your configuration file at `~/trains.conf`

Sample configuration file available [here](https://github.com/allegroai/trains/blob/master/docs/trains.conf).


## Who We Are

TRAINS is supported by the same team behind *allegro.ai*,
where we build deep learning pipelines and infrastructure for enterprise companies.

We built TRAINS to track and control the glorious but messy process of training production-grade deep learning models.
We are committed to vigorously supporting and expanding the capabilities of TRAINS.

## Why Are We Releasing TRAINS?

We believe TRAINS is ground-breaking. We wish to establish new standards of experiment management in
deep-learning and ML. Only the greater community can help us do that.

We promise to always be backwardly compatible. If you start working with TRAINS today,
even though this project is currently in the beta stage, your logs and data will always upgrade with you.

## License

Apache License, Version 2.0 (see the [LICENSE](https://www.apache.org/licenses/LICENSE-2.0.html) for more information)

## Documentation, Community & Support

More information in the [official documentation](https://allegro.ai/docs) and [on YouTube](https://www.youtube.com/c/AllegroAI).

For examples and use cases, check [examples](https://github.com/allegroai/trains/blob/master/docs/trains_examples.md).

If you have any questions: post on our [Slack Channel](https://join.slack.com/t/allegroai-trains/shared_invite/enQtOTQyMTI1MzQxMzE4LTY5NTUxOTY1NmQ1MzQ5MjRhMGRhZmM4ODE5NTNjMTg2NTBlZGQzZGVkMWU3ZDg1MGE1MjQxNDEzMWU2NmVjZmY), or tag your questions on [stackoverflow](https://stackoverflow.com/questions/tagged/trains) with '**trains**' tag.

For feature requests or bug reports, please use [GitHub issues](https://github.com/allegroai/trains/issues).

Additionally, you can always find us at *trains@allegro.ai*

## Contributing

See the TRAINS [Guidelines for Contributing](https://github.com/allegroai/trains/blob/master/docs/contributing.md).


_May the force (and the goddess of learning rates) be with you!_
