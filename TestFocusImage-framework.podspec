Pod::Spec.new do |s|
  s.name = "TestFocusImage-framework"
  s.version      =  "0.0.14"
  s.summary = "无限循环库"
  s.license = "MIT"
  s.authors = {"ChenKai"=>"kaychn@126.com"}
  s.homepage = "https://github.com/kaychn126/TestFocusImage"
  s.description = "无限循环库。。"
  s.requires_arc = true
  s.source       = { :git => "https://github.com/kaychn126/TestFocusImage.git", :tag => "#{s.version}" }

  s.ios.deployment_target    = "7.0"
  s.ios.preserve_paths       = "TestFocusImage-framework/ios/TestFocusImage.framework"
  s.ios.public_header_files  = "TestFocusImage-framework/ios/TestFocusImage.framework/Versions/A/Headers/*.h"
  s.ios.resource             = "TestFocusImage-framework/ios/TestFocusImage.framework/Versions/A/Resources/**/*"
  s.ios.vendored_frameworks  = "TestFocusImage-framework/ios/TestFocusImage.framework"
end
