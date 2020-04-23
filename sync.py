#!/usr/bin/env python3

from dirsync import sync

source_path = '/Users/valeriabonilla/Desktop/Project Sync/Screenshots'
target_path = '/Users/valeriabonilla/Desktop/Project Sync/Folder 2'

#sync(source_path, target_path, 'sync') #for syncing one way
sync(target_path, source_path, 'sync') #for syncing the opposite way
