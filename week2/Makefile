# Chọn trình mô phỏng (Icarus Verilog)
SIM ?= icarus

# Tên module testbench trong Python (không có .py)
MODULE=test_counter

# Tên module Verilog (không có .v)
TOPLEVEL=and_gate

# Danh sách file Verilog cần mô phỏng
VERILOG_SOURCES=counter.v

# Sử dụng Makefile của Cocotb để chạy mô phỏng
include $(shell cocotb-config --makefiles)/Makefile.sim
