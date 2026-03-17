
import shutil


# copy() -> copy file
shutil.copy("demo/source/file1.txt", "demo/target/file1_copy.txt")

# copytree() -> copy full folder
shutil.copytree("demo/source", "demo/source_backup", dirs_exist_ok=True)

# move() -> move file
shutil.move("demo/target/file1_copy.txt", "demo/source/file1_moved.txt")

# rmtree() -> delete folder tree
shutil.rmtree("demo/source_backup")

print("Done: copy, copytree, move, rmtree")
