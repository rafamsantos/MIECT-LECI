"""Agente v0.9"""
"""
Guilherme Craveiro nMec 103574
Rafael Santos nMec 98466
"""
import asyncio
import getpass
import json
import os

import websockets

#Custom imports
from solver import *


async def agent_loop(server_address="localhost:8000", agent_name="student"):
    
    """Server communication - Main loop"""
    async with websockets.connect(f"ws://{server_address}/player") as websocket:

        # Receive information about static game properties
        await websocket.send(json.dumps({"cmd": "join", "name": agent_name}))

        solver=Solver(websocket)
        while True:
            try:
                await solver.MainLoop()
                
            except websockets.exceptions.ConnectionClosedOK:
                print("Server has cleanly disconnected us")
                return


# DO NOT CHANGE THE LINES BELLOW
# You can change the default values using the command line, example:
# $ NAME='arrumador' python3 client.py
loop = asyncio.get_event_loop()
SERVER = os.environ.get("SERVER", "localhost")
PORT = os.environ.get("PORT", "8000")
NAME = os.environ.get("NAME",getpass.getuser())
loop.run_until_complete(agent_loop(f"{SERVER}:{PORT}", NAME))