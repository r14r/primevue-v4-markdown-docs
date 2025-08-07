<Tabs value="0" scrollable>
    <TabList>
        <Tab v-for="tab in scrollableTabs" :key="tab.title" :value="tab.value">
            {{ tab.title }}
        </Tab>
    </TabList>
    <TabPanels>
        <TabPanel v-for="tab in scrollableTabs" :key="tab.content" :value="tab.value">
            <p class="m-0">{{ tab.content }}</p>
        </TabPanel>
    </TabPanels>
</Tabs>