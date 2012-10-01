#!/bin/bash

# CONFIGURATION
REMOTE_URL="https://github.com/sureshadichithara/demo-new.git"
START_DATE="2012-10-01"
END_DATE="2012-10-02"



# Initial commit to create the main branch
touch .gitkeep
git add .gitkeep
git commit -m "Initial commit"

# STEP 2: Gather all valid files (skip hidden/system files)
mapfile -t FILES < <(find . -type f -not -path "*/\.*" -not -path "./.git/*")
TOTAL_FILES=${#FILES[@]}
INDEX=0

# Create or clear log files
> skipped_files.log
> commit_log.txt

# STEP 3: Begin committing
CURRENT_DATE="$START_DATE"
while [[ "$CURRENT_DATE" < "$END_DATE" && $INDEX -lt $TOTAL_FILES ]]; do
  SKIP=$(( RANDOM % 3 ))  # 0 to 2, skip on 0

  if [[ $SKIP -eq 0 ]]; then
    echo "[$CURRENT_DATE] Skipping day" | tee -a commit_log.txt
  else
    COMMITS=$(( (RANDOM % 3) + 1 ))  # 1 to 3 commits max
    for ((i = 1; i <= COMMITS && INDEX < TOTAL_FILES; i++)); do
      FILE="${FILES[$INDEX]}"
      CLEAN_NAME="${FILE#./}"

      # Check if it's a regular file
      if [[ -f "$FILE" ]]; then
        export GIT_AUTHOR_DATE="$CURRENT_DATE 12:0$i:00"
        export GIT_COMMITTER_DATE="$CURRENT_DATE 12:0$i:00"

        echo "[$CURRENT_DATE] Committing: $CLEAN_NAME" | tee -a commit_log.txt
        git add -f "$FILE"
        git commit -m "$CLEAN_NAME"
        ((INDEX++))
      else
        echo "[$CURRENT_DATE] Skipping invalid file: $FILE" | tee -a skipped_files.log
      fi
    done
  fi

  # Advance to next day
  CURRENT_DATE=$(date -I -d "$CURRENT_DATE + 1 day")
done

# STEP 4: Push to GitHub
git push -u origin main