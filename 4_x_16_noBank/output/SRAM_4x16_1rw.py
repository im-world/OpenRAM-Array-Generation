num_rw_ports    = 1
num_r_ports     = 0
num_w_ports     = 0

word_size       = 4
num_words       = 16
#num_banks       = 1
#words_per_row   = 8

tech_name       = "freepdk45"
process_corners = ["TT"]
supply_voltages = [1.1]
temperatures    = [25]

route_supplies  = True
check_lvsdrc    = False

output_path     = "output"
output_name     = "SRAM_4x16_1rw"
instance_name   = "SRAM_4x16_1rw"
