/* eslint no-console: 0, no-undef: 0, no-unused-vars: 0 */
/* Find all references to Sweet Victory / Spongebob */

const targetNode = document.body;

// Options for the observer (which mutations to observe)
const config = {
  attributes: false,
  childList: true,
  subtree: false,
  characterData: false,
};

// Callback function to execute when mutations are observed
let callback = (mutationsList, observer) => {
  for (const mutation of mutationsList) {
    //modifyReferences(mutation);
    if (/sweet victory/ig.test(mutation.target.innerHTML)) {
      modifyReferences(mutation.target);
    }
  }
};

/* Find all references to Sweet Victory in the current page... */
const modifyReferences = (rootNode) => {
  const backup = rootNode.innerHTML;
  try {
    rootNode.innerHTML = rootNode.innerHTML.replace(/sweet victory/ig, 'sicko mode');
  } catch (err) {
    rootNode.innerHTML = backup;
  }
};

const setupObserver = () => {
  const observer = new MutationObserver(callback);
  observer.observe(targetNode, config);
};

const main = () => {
  /* Do an inital run */
  modifyReferences(targetNode);
  /* Setup the observer */
  setupObserver();
};


main();
