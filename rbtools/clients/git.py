    name = 'Git'

                                 'HEAD'], ignore_errors=True).strip()
        if (not getattr(self.options, 'repository_url', None) and
        if self.head_ref:
            short_head = self._strip_heads_prefix(self.head_ref)
            merge = execute([self.git, 'config', '--get',
                             'branch.%s.merge' % short_head],
                            ignore_errors=True).strip()
            remote = execute([self.git, 'config', '--get',
                              'branch.%s.remote' % short_head],
                             ignore_errors=True).strip()

            merge = self._strip_heads_prefix(merge)
            if remote and remote != '.' and merge:
                self.upstream_branch = '%s/%s' % (remote, merge)
        if getattr(self.options, 'repository_url', None):
        upstream_branch = (getattr(self.options, 'tracking', None) or
        head_ref = "HEAD"
        if self.head_ref:
            head_ref = self.head_ref
                                   head_ref]).strip()
            diff_lines = self.make_diff(self.merge_base, head_ref)
        if (getattr(self.options, 'guess_summary', None) and
            not getattr(self.options, 'summary', None)):
        if (getattr(self.options, 'guess_description', None) and
            not getattr(self.options, 'description', None)):
            cmdline = [self.git, "diff", "--no-color", "--full-index",
                       "--no-ext-diff", "--ignore-submodules", "--no-renames",
                       rev_range]

            if (self.capabilities is not None and
                self.capabilities.has_capability('diffs', 'moved_files')):
                cmdline.append('-M')

            return execute(cmdline)
        head_ref = "HEAD"
        if self.head_ref:
            head_ref = self.head_ref

                                   head_ref]).strip()

    def apply_patch(self, patch_file, base_path=None, base_dir=None, p=None):
        """
        Apply the patch patch_file and return True if the patch was
        successful, otherwise return False.
        """
        if p:
            cmd = ['git', 'apply', '-p', p, patch_file]
        else:
            cmd = ['git', 'apply', patch_file]

        self._execute(cmd)