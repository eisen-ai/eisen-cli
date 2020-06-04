import click

from eisen_cli.train import eisen_training


@click.group()
def cli():
    pass


@click.command()
@click.argument('configuration')
@click.argument('epochs', default=10)
@click.option('--data_dir', default='./data', help='base directory where to data is placed')
@click.option('--artifact_dir', default='./artifacts', help='base directory where to store/read the artifacts')
@click.option('--resume', default=False, help='resume training from specified model training artifacts')
def train(configuration, epochs, data_dir, artifact_dir, resume):
    """
    Command line interface (CLI) for model training. This utility allows to train a model by specifying a
    configuration file. Configuration files need to be in JSON format and can be obtained by visual experiment
    building using the utility at http://builder.eisen.ai

    example usage for 100 epochs, training with config.json, /data and /artifacts as data path and artifact path.

    .. code-block:: console

        $ eisen train config.json 100 --data_dir /data --artifact_dir /artifacts --resume false

    :param configuration: Path of JSON configuration file
    :type configuration: Path
    :param epochs: Number of training epochs
    :type epochs: int
    :param data_dir: Directory path representing the data "base" path
    :type data_dir: Path
    :param artifact_dir: Directory path where the results of the training shall be stored
    :type artifact_dir: Path
    :param resume: Whether the artifact_dir should be used to load a model and resume training
    :type resume: bool

    :return: None
    """
    eisen_training(configuration, epochs, data_dir, artifact_dir, resume)


@click.command()
@click.argument('configuration')
@click.option('--data_dir', default='./data', help='base directory where to data is placed')
@click.option('--artifact_dir', default='/results/experiment', help='directory where model training artifacts reside')
def validate(configuration, data_dir, artifact_dir):
    pass


@click.command()
@click.argument('configuration')
@click.option('--data_dir', default='./data', help='base directory where to data is placed')
@click.option('--artifact_dir', default='/results/experiment', help='directory where model training artifacts reside')
def test(configuration, data_dir, artifact_dir):
    pass


@click.command()
@click.argument('configuration')
@click.option('--artifact_dir', default='/results/experiment', help='directory where model training artifacts reside')
def serve(configuration, artifact_dir):
    pass


cli.add_command(train)
cli.add_command(validate)
cli.add_command(test)
cli.add_command(serve)


if __name__ == '__main__':
    cli()
