<Tabs value="0">
    <TabList>
        <Tab v-for="tab in tabs" :key="tab.title" :value="tab.value">{{ tab.title }}</Tab>
    </TabList>
    <TabPanels>
        <TabPanel v-for="tab in tabs" :key="tab.content" :value="tab.value">
            <p class="m-0">{{ tab.content }}</p>
        </TabPanel>
    </TabPanels>
</Tabs>