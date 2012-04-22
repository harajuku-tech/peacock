#!/bin/bash

export RUNPORT=8900

RUN()
{
 python ../manage.py runsever 0.0.0.0:$RUNPORT
}
