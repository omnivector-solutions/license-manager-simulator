#!/usr/bin/env bash

# Python executable path
python_path="#\!\/srv\/license-manager-agent-venv\/bin\/python3.8"
# Path where the templates and scripts will be copied to
file_path="\/srv\/license-manager-agent-venv\/lib\/python3.8\/site-packages\/bin"
# License Manager Simulator IP address
lm_sim_ip="http:\/\/192.168.0.37:8000"

# Folder names (one for each license server supported)
folders=(
	"flexlm"
	"rlm"
	"lsdyna"
	"lmx"
)

# Scripts that will be copied to the machine
scripts=(
	"lms-util.py"
	"rlm-util.py"
	"lsdyna-util.py"
	"lmx-util.py"
)

# License server binary names (will be simulated using the scripts)
binary_names=(
	"lmutil"
	"rlmutil"
	"lstc_qrun"
	"lmxendutil"
)

# Template files that will render information retrieved from the simulator backend
templates=(
	"flexlm.out.tmpl"
	"rlm.out.tmpl"
	"lsdyna.out.tmpl"
	"lmx.out.tmpl"
)

# Changing path and ip address in script files
for script in ${scripts[@]}; do
	echo "Updating $script file"
	sed -i "s/#\!\/usr\/bin\/env python3/$python_path/gi" $script
	sed -i "s/(\".\")/(\"$template_path\")/gi" $script
	sed -i "s/http:\/\/localhost:8000/$lm_sim_ip/gi" $script
done

# Copying script and template files to machine
juju ssh license-manager-agent/leader mkdir /tmp/simulator-files

for folder in ${folders[@]}; do
	echo "Copying files from $folder to license-manager-agent machine"
	juju scp -- -r $folder license-manager-agent/leader:/tmp/simulator-files
done

# Moving files to correct location and adding executable permission
for i in {0..3}; do
	echo "Moving ${scripts[$i]} script file and renaming to ${binary_names[$i]}"
	juju ssh license-manager-agent/leader sudo mv /tmp/simulator-files/${folders[$i]}/${scripts[$i]} $file_path/${binary_names[$i]}

	echo "Adding executable permission to ${binary_names[$i]} file"
	juju ssh license-manager-agent/leader sudo chmod +x $file_path/${binary_names[$i]}

	echo "Moving template ${templates[$i]}"
	juju ssh license-manager-agent/leader sudo mv /tmp/simulator-files/${folders[$i]}/${templates[$i]} $file_path
done

# Deleting temporary folders
echo "Deleting temporary simulator files"
juju ssh license-manager-agent/leader rm -rf /tmp/simulator-files

echo "All done!"
