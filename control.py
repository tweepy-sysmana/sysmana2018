#!/usr/bin/env python
# -*- coding: utf-8 -*-

# devuelve un analisis de las relaciones de un usuario en base a un historico previo (seguidores, amigos, seguidores inactivos, antiguos seguidores...)
import sys, tweepy, shelve, datetime, traceback
import itertools # Librería de Python con métodos que devuelven iterables eficientes.

def get_followers(api):
    # api = init_twitter('nieves')
    followers = {}
    friendsIds = []
    lostFollowers = {}
    newFollowers = {}
    followerIds = []
    inactivos = []
    #fichero donde guardamos el historico
    followersFile = 'followers_control.twt'
    user = sys.argv[1]
    inactivityTime = 90 #dias que establecemos para inactividad de un usuario
    today = datetime.datetime.now()


    def paginacion(iterable, pageSize):
        while True:
            i1, i2 = itertools.tee(iterable)
            iterable, page = (itertools.islice(i1, pageSize, None),
                list(itertools.islice(i2, pageSize)))
            if len(page) == 0:
                break
            yield page #devolvemos ese iterable

    if len(sys.argv) != 2:
    sys.exit('Usage: '+sys.argv[0]+' twitter_user')


    # Recoge la información de usuario
    try:
    userInfo = api.get_user(user)
    except tweepy.error.TweepError, e:
    traceback.print_exc()
    if e.reason == 'Not found':
        sys.exit('Error: Usuario no encontrado!!')
    elif e.reason.find('Rate limit exceeded'):
        sys.exit('Error: Limite excedido')
    else:
        sys.exit('Error: '+str(e.reason))

    usuario = userInfo.name
    idioma = userInfo.lang
    ubicacion = userInfo.location
    if ubicacion == None:
    ubicacion = '-'
    userTimeZone = userInfo.time_zone
    if userTimeZone == None:
    userTimeZone = '-'
    if userInfo.protected:
    actividad = '-'
    else:
    try:
        actividad = str(userInfo.status.created_at)
    except:
        try:
            timeLine = userInfo.timeline()
        except tweepy.error.TweepError, e:
            print str(sys.exc_info())
            sys.exit('Error: '+str(e.reason))
        if timeLine != []:
            actividad = str(timeLine[0].created_at)
        else:
            actividad = '-'
    userCreation = str(userInfo.created_at)
    if userCreation == None:
    userCreation = '-'
    if userInfo.protected:
    print 'cuenta protegida, imposible comprobar amigos y followers.'

    try:
    ## Comprobamos followers nuevos y perdidos
    # Tomamos los ids de nuestros follower
    followersCursor = tweepy.Cursor(api.followers_ids,id=user)
    for id in followersCursor.items():
        followerIds.append(id)

    # Comprobación con antiguos followers
    oldFollowers = shelve.open(followersFile)
    if oldFollowers.has_key(user):
        oldFollowersByUser = oldFollowers[user]
        followers = dict(oldFollowersByUser)
        for followerId in oldFollowersByUser:
            if followerId not in followerIds:
                lostFollowers[followerId] = oldFollowersByUser[followerId]
                followers.pop(followerId)
        for followerId in followerIds:
            if followerId not in oldFollowersByUser:
                newFollowers[followerId] = []
    else:
        print 'No hay fichero histórico previo, va a generarse uno nuevo..\n'

    # Información de los nuevos followers
    newFollowersIds = newFollowers.keys()
    for newFollowersPage in paginacion(newFollowersIds, 100):
        newFollowersObjects = api.lookup_users(user_ids=newFollowersPage)
        for newFollower in newFollowersObjects:
            newFollowers[newFollower.id] = [newFollower.name, newFollower.screen_name]

    followers.update(newFollowers)
    oldFollowers[user] = followers
    oldFollowers.close()

    ## Amigos
    # Tomamos los ids de los amigos
    friendsCursor = tweepy.Cursor(api.friends_ids,id=user)
    for id in friendsCursor.items():
        friendsIds.append(id)

    # Información de cada amigo
    for friendsPage in paginacion(friendsIds, 100):
        friendsObjects = api.lookup_users(user_ids=friendsPage)
        for friend in friendsObjects:
                inactivity = None
                inactivityDate = None
                if not friend.protected:
                    try:
                        inactivity = today - friend.status.created_at
                        inactivityDate = str(friend.status.created_at)
                    except:
                        timeLine = friend.timeline()
                        if timeLine != []:
                            inactivity =  today - timeLine[0].created_at
                            inactivityDate =  str(timeLine[0].created_at)
                        else:
                            inactivity =  today - friend.created_at
                            inactivityDate = str(friend.created_at)
                    if inactivity != None and inactivity.days > inactivityTime:
                        inactivos.append([friend.name,friend.screen_name,inactivityDate])

    except tweepy.error.TweepError, e:
    if e.reason.find('Rate limit exceeded') != -1:
        sys.exit('Error: Límite excedido')
    else:
        sys.exit('Error: '+str(e.reason))

    # Informacion del usuario
    # print '###############################################'
    # print 'Usuario: '+user
    # print 'Nombre: '+usuario
    # print 'Ubicacion: '+ubicacion
    # print 'Idioma: '+idioma
    # print 'Time Zone: '+userTimeZone
    # print 'Creado: '+userCreation
    # print 'Ultimo tweet: '+actividad
    # print '###############################################'
    # print

    # Amistades
    # print '###############################################'
    # print 'Número de amigos: '+str(len(friendsIds))
    # if inactivos == []:
    #    print 'Amigos inactivos: 0'
    # else:
    #    print 'Amigos inactivos en '+str(inactivityTime)+' días ('+str(len(inactivos))+'):'
    #    inactivos = sorted(inactivos, key = lambda x:x[2])
    #    for inactive in inactivos:
    #       print '\t['+inactive[2]+'] '+inactive[0]+' ('+inactive[1]+')'
    # print '###############################################'
    # print

    # Followers
    # print '###############################################'
    # print 'Followers: '+str(len(followers))
    # if newFollowers == []:
    #    print 'Nuevos Followers: 0'
    # else:
    #    print 'Nuevos Followers ('+str(len(newFollowers))+'):'
    #    for newFollowerId in newFollowers:
    #       newFollowerName, newFollowerScreenName = newFollowers[newFollowerId]
    #       print '\t'+newFollowerName+' ('+newFollowerScreenName+')'
    # if lostFollowers == []:
    #    print 'Followers Perdidos: 0'
    # else:
    #    print 'Followers Perdidos ('+str(len(lostFollowers))+'):'
    #    for lostFollowerId in lostFollowers:
    #       lostFollowerName, lostFollowerScreenName = lostFollowers[lostFollowerId]
    #       print '\t'+lostFollowerName+' ('+lostFollowerScreenName+')'
    # print '###############################################'
    # print
