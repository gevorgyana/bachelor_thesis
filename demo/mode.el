(defun record-voice-note ()
  "This function uses ALSA sound tools to record voice notes. The
concept is more important than which tools are used. It starts
recording the sound file within emacs. It can be your sound
note. Once you press `q` it will stop recording, and open up the
directory with sound files"
  (interactive)
  (let* (
	 (buffer "*Sound Recording*"))
    (switch-to-buffer buffer)
    (erase-buffer)
    (setq-local header-line-format "➜ Finish recording with 'q'")
    (let* ((process (start-process-shell-command buffer buffer "arecord sound.wav")))
      (local-set-key "q" (lambda () (interactive) (kill-process process nil)
			   (local-set-key "q" 'kill-current-buffer)
			   (find-file filepath)
			   (revert-buffer)))
      (recursive-edit))))
