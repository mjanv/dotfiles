return {
  {
    -- Shade of purples
    "Rigellute/shades-of-purple.vim",
    lazy = false,
    priority = 1100,
    config = function()
      vim.cmd.colorscheme "shades_of_purple"
    end
  },
  {
    "catppuccin/nvim",
    lazy = false,
    name = "catppuccin",
    priority = 1000,
    config = function()
      vim.cmd.colorscheme "catppuccin"
    end
  }
}
