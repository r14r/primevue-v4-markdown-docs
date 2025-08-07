const CustomPreset = usePassThrough(
    BasePreset,
    {
        panel: {
            header: 'my_panel_header'
        }
    },
    { mergeSections: false, mergeProps: false }
);

// Output:
// panel.header.class => 'my_panel_header'
// panel.title.class => undefined