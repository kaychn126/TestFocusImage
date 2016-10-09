Pod::Spec.new do |s|
  s.name = "TestFocusImage-framework"
  s.version      =  "0.0.12"
  s.summary = "无限循环库"
  s.license = "MIT"
  s.authors = {"ChenKai"=>"kaychn@126.com"}
  s.homepage = "https://github.com/kaychn126/TestFocusImage"
  s.description = "无限循环库。。"
  s.requires_arc = true
  s.source       = { :git => "https://github.com/kaychn126/TestFocusImage.git", :tag => "#{s.version}" }

  s.ios.deployment_target    = "7.0"
  s.ios.preserve_paths       = "TestFocusImage-0.0.11/ios/TestFocusImage.framework"
  s.ios.public_header_files  = "TestFocusImage-0.0.11/ios/TestFocusImage.framework/Versions/A/Headers/*.h"
  s.ios.resource             = "TestFocusImage-0.0.11/ios/TestFocusImage.framework/Versions/A/Resources/**/*"
  s.ios.vendored_frameworks  = "TestFocusImage-0.0.11/ios/TestFocusImage.framework"
end