import os

import click
import tweepy

from .getLocation import MyStreamListener
from .horasActivas import horas
from .favorite import MyStreamListener as FavoriteListener
from .retuitea import retweet
from .streamSearch import MyStreamListener as StreamStreamListener
from .twitter_client import TwitterAuthApi


# TODO
client = TwitterAuthApi(credentials)


@click.group()
def cli():
    pass


@click.command()
def control():
    get_followers(client.get_user_api(user))


@click.command()
def favourite():
    api = client.get_user_api('sysmanapy')
    myStreamListener = FavoriteListener()
    myStream = tweepy.Stream(
        auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['sysmana2018'])


@click.command()
def location():
    api = client.get_user_api('sysmanapy')
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['sysmana2018'])


@click.command()
def activehours():
	horas(user)


@click.command()
def retuitea():
    # TODO Needs to handle files
    retweet(ftuits)


@click.command()
def stream():
	myStreamListener = StreamStreamListener() #### PASO 3
	myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener) #### PASO 4
	myStream.filter(track=['sysmana2018']) #### PASO 5


if __name__ == '__main__':
    cli.add_command(control)
    cli.add_command(favourite)
    cli.add_command(location)
    cli.add_command(activehours)
    cli.add_command(retuitea)
    cli.add_command(stream)
    cli()