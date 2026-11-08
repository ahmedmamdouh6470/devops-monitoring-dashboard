#!/bin/bash

echo "================================"
echo "DevOps System Health Check"
echo "================================"

echo ""
echo "Hostname:"
hostname

echo ""
echo "Current User:"
whoami

echo ""
echo "System Uptime:"
uptime

echo ""
echo "Disk Usage:"
df -h /

echo ""
echo "Memory Usage:"
free -h

echo ""
echo "System Check Completed"
