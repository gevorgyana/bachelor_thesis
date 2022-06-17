;; https://gnu.support/gnu-emacs/emacs-lisp/Emacs-Lisp-Record-voice-notes-within-GNU-Emacs.html
;; like here
;; This mode should be loaded into Emacs with

(defvar sound-recordings-dir "/home/data1/protected/Media/Sound/Recordings/"
  "This is your sound recording directory. Keep slash on the end")

(defvar sound-recording-extension ".ogg"
  "This is your sound file extension")

(defun record-voice-note ()
  "This function uses SOX sound tools to record voice notes. The
concept is more important than which tools are used. It starts
recording the sound file within emacs. It can be your sound
note. Once you press `q` it will stop recording, and open up the
directory with sound files"
  (interactive)
  (let* ((filepath (concat sound-recordings-dir (format-time-string "%Y/%m/%Y-%m-%d/")))
     (filename (concat filepath (format-time-string "%Y-%m-%d-%H:%M:%S") sound-recording-extension))
         (command-1 (voice-record-command filename))
     (buffer "*Sound Recording*"))
    (make-directory filepath t)
    (switch-to-buffer buffer)
    (erase-buffer)
    (setq-local header-line-format "➜ Finish recording with 'q'")
    (let* ((process (start-process-shell-command buffer buffer command-1)))
      (local-set-key "q" (lambda () (interactive) (kill-process process nil)
               (local-set-key "q" 'kill-current-buffer)
               (find-file filepath)
               (revert-buffer)))
      (recursive-edit))))

(defun voice-record-command (filename &optional rate channels)
  "Returns sound recording command with default rate and channels"
  (let* ((rate (if rate rate 16000))
     (channels (if channels channels 1))
     (command (format "arecord" user-full-name filename rate channels filename)))
    command))
