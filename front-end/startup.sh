#!/bin/bash

if $IS_LIVE ; then
    echo 'Running production'
    npm run build
    npm start
else
   echo 'Running development'
   npm run dev
fi