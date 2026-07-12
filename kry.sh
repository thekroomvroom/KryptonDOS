clear

os=$(uname -s)

if command -v python3 &> /dev/null; then
    locat="./dos/dep/pylib.txt"
    pip3 install -r "$locat"
    if [ "$os" = "Darwin" ]; then
        if command -v clang &> /dev/null; then
            clang ./dos/kry.c -o kry
            chmod +x kry
            ./kry
            rm kry.sh
        else
            echo "Seems like Clang is not installed."
            read -p "Would you like to install it? (y/n) " cyn
            cyn=$(echo "$cyn" | tr '[:upper:]' '[:lower:]')
            if [ "$cyn" = "y" ]; then
                xcode-select --install
                exec "$0"
            else
                exit
            fi
        fi
    else
        if command -v gcc &> /dev/null; then
            gcc ./dos/kry.c -o kry
            chmod +x kry
            ./kry
            rm kry.sh
        else
            echo "Seems like Gcc is not installed."
            read -p "Would you like to install it? (y/n) " cyn
            cyn=$(echo "$cyn" | tr '[:upper:]' '[:lower:]')
            if [ "$cyn" = "y" ]; then
                echo "Select your Linux Distribution:"
                echo "---------------------------------"
                echo "1. Ubuntu/Debian"
                echo "2. Arch Linux"
                echo "3. Fedora Linux/Red Hat Linux"
                echo "4. Other Linux Distributions/ BSD"
                read -p "[?]: " ld
                if [ "$ld" = "1" ]; then
                    sudo apt update && sudo apt upgrade
                    sudo apt install gcc
                    exec "$0"
                elif [ "$ld" = "2" ]; then
                    sudo pacman -Syu
                    sudo pacman -S gcc
                    exec "$0"
                elif [ "$ld" = "3" ]; then
                    sudo dnf upgrade
                    sudo dnf install gcc
                    exec "$0"
                elif [ "$ld" = "4" ]; then
                    echo "Enter Installation Command:"
                    read -p " $ " ic
                    clear
                    sudo "$ic"
                    exec "$0"
                else
                    echo "Invalid Input"
                    exit
                fi
            else
                exit
            fi
        fi
    fi

else
    echo "Seems like python3 is not installed"
    echo "Please install it before launching the script"
    exit
fi