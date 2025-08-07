<Splitter style="height: 300px">
    <SplitterPanel class="flex items-center justify-center" :size="20" :minSize="10"> Panel 1 </SplitterPanel>
    <SplitterPanel :size="80">
        <Splitter layout="vertical">
            <SplitterPanel class="flex items-center justify-center" :size="15"> Panel 2 </SplitterPanel>
            <SplitterPanel :size="85">
                <Splitter>
                    <SplitterPanel class="flex items-center justify-center" :size="20"> Panel 3 </SplitterPanel>
                    <SplitterPanel class="flex items-center justify-center" :size="80"> Panel 4 </SplitterPanel>
                </Splitter>
            </SplitterPanel>
        </Splitter>
    </SplitterPanel>
</Splitter>